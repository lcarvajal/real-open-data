function makeChart() {
    let chartData = JSON.parse(document.getElementById('chart-data').textContent);

    console.log(chartData)
    console.log(typeof chartData)
    var chart = new Chart('chart', {
        type: chartData.type,
        options: {
            maintainAspectRatio: false,
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    scaleLabel: {
                    display: true,
                    labelString: chartData.y_title,
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                    display: true,
                    labelString: chartData.x_title,
                    }
                }]
            }
        },
        data: chartData.json_data
    });
}

function updateChart(val) {
    let filterOption = $('#filter').find(":selected").val();
    let url = $('#filter').data('url');
    window.location.replace(url.replace('temp', filterOption))
}

makeChart();