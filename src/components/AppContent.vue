<template>
    <div id="content" class="columns is-mobile is-vcentered" style="min-height: 80vh;">
        <h1 class = "title is-1" style = "position: absolute; text-align: center; margin-left: 5%; margin-top: -20%; max-width: 30%">
            Negotiate your medical bills with transparent pricing data.</h1>
            <h1 class = "subtitle is-3" style ="position: absolute; text-align: center; margin-left: 50%; margin-top: 30%; max-width: 30%">
                You do not need to be a medical expert to understand your bill.
            </h1>
        <div class="column">
            <img src="../assets/undraw_doctor_kw-5-l.svg" style="position: absolute; bottom: -12rem; left: -20rem; z-index: -1; scale: 40%">
        </div>
        <div class="column">
            <img src="../assets/undraw_receipt_re_fre3.svg" style="position: absolute; bottom: 0rem; right: -5rem; z-index: -1; scale: 80%">
        </div>
        <div class = "columns is-hcentered" style="width: 58%">
        <!-- File Upload -->
            <div id='file-select' class="levels mt-4">
                <div class="file has-name is-boxed mb-2 level-item">
                    <label class="file-label">
                        <input class="file-input" type="file" name="resume" accept=".pdf" v-on:change="setFile()">
                        <span class="file-cta">
                        <span class="file-icon">
                            <i class="fas fa-upload"></i>
                        </span>
                        <span class="file-label">
                            Upload Medical Bill
                        </span>
                        </span>
                        <span class="file-name">
                        
                        </span>
                    </label>
                </div>
                <button id='file-submit' class="button is-primary is-large ml-2" disabled = "true" v-on:click="fileButtonPress()">Analyze Medical Bill</button>
            </div>
        </div>
    </div>
    <!-- Table -->
    <app-table/>
</template>

<script>
    import AppTable from './AppTable.vue'
    import axios from 'axios'

    const getFile = () => {
        return document.querySelector('.file-input').files.item(0);
    }
    const setFile = () => {
        const file = getFile();
        const fileLabel = document.querySelector('.file-name');
        fileLabel.textContent = file.name;
        document.getElementById('file-submit').disabled = false;
    }
    /* const handleFile = () => {
        document.querySelector('#content').classList.add('is-hidden');
        document.querySelector('#table-container').classList.remove('is-hidden');
        const data = [['80050', 'General health panel', '$201', '0'], 
                        ['84439', 'Thyroxine (thyroid chemical), free', '$55', '0'], 
                        ['83206', 'Vitamin D-3 Level', '$207', 0], 
                        ['80061', 'Blood Test, Lipids (cholesterol and triglycerides)', '$80', getNumber(0)], 
                        ['99396', 'Established patient periodic preventive medicine examination (40-64 years)', '$455', getNumber(5)]
                    ];
        console.log(data);
        //Parse PDF grabbing file with getFile() to get data
        generateTableRows(data);
    } */

    function getDescription(code) {
        let url = "https://us-central1-cruzhacks2022-338309.cloudfunctions.net/cpt_decription?code=" + code;
        return new Promise(function (resolve, reject) {
            axios.get(url).then(
                (response) => {
                    var result = response.data;
                    resolve(result);
                },
                    (error) => {
                    reject(error);
                }
            );
        });
    }
    async function getDict(encodedPDF){
        let url = "https://us-central1-cruzhacks2022-338309.cloudfunctions.net/parsePDF";
        return new Promise(function (resolve, reject) {
            axios.post(url, { "pdf-data": encodedPDF }).then(response => {
                var result = response.data;
                resolve(result);
            }, 
                (error) => {
                    reject(error);
                })
        });
    }

    async function readPDF(file){
        return new Promise(function (resolve) {
            var reader = new FileReader();
            reader.onload=function(){
                var res = btoa(reader.result); // base 64
                resolve(res);
            };
            reader.readAsBinaryString(file);
        })
    }

    async function getAvgCost(code){
        let url = "https://us-central1-cruzhacks2022-338309.cloudfunctions.net/get_price?code=" + code;
        return new Promise(function (resolve, reject) {
            axios.get(url).then(
                (response) => {
                    var result = response.data;
                    resolve(result);
                },
                    (error) => {
                    reject(error);
                }
            );
        });
    }

    async function fileButtonPress(){
        document.querySelector('#content').classList.add('is-hidden');
        document.querySelector('#loading-bar').classList.remove('is-hidden');
        // show loading screen

        // We need to parse the pdf
        // We need to get the file that the user inputted
        console.log(getFile())

        var result = await readPDF(getFile());
        console.log(result);
        //console.log(await getDict2(res));
        var dict = await getDict(result);
        console.log(dict);
        var data = [];
        var actualCost = 0.0;
        var averageCost = 0.0;
        for (var f in dict){
            // We want to push an array of size 4 for every code we got
            var a = await getAvgCost(f);
            console.log(f)
            data.push([f, await getDescription(f), '$' + dict[f], '$' + a]);
            averageCost += parseFloat(a);
            actualCost += parseFloat(dict[f]);
        }
        console.log(averageCost);
        console.log(actualCost);

        generateTableRows(data);
        document.querySelector('#loading-bar').classList.add('is-hidden');
        document.querySelector('#table-container').classList.remove('is-hidden');
        if(averageCost > actualCost){
            document.querySelector('#saved-value').classList.remove('is-hidden');
        }
        else{
            document.querySelector('#lost-value').classList.remove('is-hidden');
        }
    }

    function generateTableRows(data) {
        
        const tableBody = document.querySelector('#tableBody');
        data.forEach((item) => {
            const row = document.createElement('tr');
            for(let i = 0; i < 4; i++){
                const cell = document.createElement('td');
                cell.textContent = item[i];
                row.append(cell);
            }
            
            tableBody.append(row);
        });
    }
    export default {
        components: {
            AppTable,
        },
        methods: {
            getFile,
            setFile,
            fileButtonPress,
            generateTableRows,
        }
    }
</script>
