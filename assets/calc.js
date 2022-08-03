$(function() {
    startRefresh();
});

function startRefresh() {
    setTimeout(startRefresh,1000);


    var kwh_price = parseInt($('#range-slider__value1').html()),
        wat_classic = parseInt($('#range-slider__value2').html()),
        wat_led = parseInt($('#range-slider__value3').html()),
        led_p = parseInt($('#range-slider__value4').html()),
        number = parseInt($('#range-slider__value5').html()),
        avg_day = parseInt($('#range-slider__value6').html());

    var classic = kwh_price * wat_classic * avg_day * number*30/1000;
    var led = kwh_price * wat_led * avg_day * number *30/1000;
    var led_price = number * led_p;




    var myChart = echarts.init(document.getElementById('calculator-container-graph-graph'));


    var colors = ['#14b1ef', '#ffc807', '#000000'];


    option = {

        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:['LED','Klasická']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: [0,1,2,3,4,5,6,7,8,9,10,11,12]
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name:'LED',
                type:'line',
                color:'#5793f3',
                data: [0*led+led_price,1*led+led_price,2*led+led_price,3*led+led_price,4*led+led_price,5*led+led_price,6*led+led_price,7*led+led_price,8*led+led_price,9*led+led_price,10*led+led_price,11*led+led_price,12*led+led_price]
            },
            {
                name:'Klasická',
                type:'line',
                color:'#ffc807',
                data: [0*classic,1*classic,2*classic,3*classic,4*classic,5*classic,6*classic,7*classic,8*classic,9*classic,10*classic,11*classic,12*classic]
            }
        ]
    };

    myChart.setOption(option);

}
