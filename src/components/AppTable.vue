<template>
    <div id="table-container" class="containter is-hidden">
        <table width="100%" class="table is-fullwidth" style="font-size: 150%" id="dataTable">
            <thead>
                <tr>
                    <th>CPT Code</th>
                    <th>Service Received</th>
                    <th>Amount Billed</th>
                    <th>Average Cost</th>
                </tr>
            </thead>
            <tbody id="tableBody"></tbody>
        </table>
        <div id="saved-value" class="box mt-6 has-background-success is-hidden">
            <p class="title has-text-white">Your cost was {{TOTAL_SAVINGS}} less than the average in your area.</p>
        </div>
        <div id="lost-value" class="box mt-6 has-background-success is-hidden">
            <p class="title has-text-white">Your cost was {{TOTAL_LOSS}} more than the average in your area.</p>
        </div>
        
    </div>
    <div id="loading-bar" class="is-hidden" style="max-width: 40%; margin: auto">
            <progress class="progress is-large is-info" max="100">5%</progress>
            <p class="title has-text-black">
                We are scanning your pdf and comparing prices in your area.
            </p>
        </div>
</template>
