function make_Chart(element_ID, headers, data) {
    var ctx = document.getElementById(element_ID).getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: headers,
    datasets: [{
        label: 'NonCurrent Assets',
        data: data,
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
        borderWidth: 1
    }]
},
})
    ;

}
