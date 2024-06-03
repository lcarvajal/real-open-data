function makeChart() {
    let chart = JSON.parse(document.getElementById('chart-data').textContent);

    // Using Chart.js to create a chart
    new Chart('chart', {
        type: chart.type,
        options: {
            maintainAspectRatio: false,
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    scaleLabel: {
                    display: true,
                    labelString: chart.y_title,
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                    display: true,
                    labelString: chart.x_title,
                    }
                }]
            }
        },
        data: {
            labels: chart.x_labels,
            datasets: [{
                data: chart.y_values
            }]
        }
    });
}

function updateChart(val) {
    let filterOption = $('#filter').find(":selected").val();
    let url = $('#filter').data('url');
    window.location.replace(url.replace('temp', filterOption))
}

makeChart();