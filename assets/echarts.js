// based on prepared DOM, initialize echarts instance
var myChart = echarts.init(document.getElementById('main'));

// specify chart configuration item and data

option = {
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: ['LED', 'Klasická']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'value',
        boundaryGap: [0, 0.01]
    },
    yAxis: {
        type: 'category',
        data: ['1300lm', '800lm', '500lm']
    },

    series: [
        {
            name: 'LED',
            type: 'bar',
            color: '#239ceb',
            data: [12, 10, 7]
        },
        {
            name: 'Klasická',
            type: 'bar',
            color: '#ffc807',
            data: [100, 60, 40]
        }
    ]
};


// use configuration item and data specified to show chart
myChart.setOption(option);
