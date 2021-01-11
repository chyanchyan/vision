// Initialize Realtime Chart

var ChartID = "realtime_loan_outstanding"
var realTimeData = [];
var totalPoints = 300;
var updateInterval = 30;

function getData() {
    if (realTimeData.length > 0)
        realTimeData = realTimeData.slice(1);

    // Do a random walk

    while (realTimeData.length < totalPoints) {
        var prev = realTimeData.length > 0 ? realTimeData[realTimeData.length - 1] : 50,
            y = prev + Math.random() * 10 - 5;

        if (y < 0) {
            y = 0;
        } else if (y > 100) {
            y = 100;
        }

        realTimeData.push(y);
    }

    // Zip the generated y values with the x values

    var res = [];
    for (var i = 0; i < realTimeData.length; ++i) {
        res.push([i, realTimeData[i]])
    }

    return res;
}

var options8 = {
    colors: ['#a2d200'],
    series: {
        shadowSize: 0,
        lines: {
            show: true,
            fill: 0.1
        }
    },
    xaxis: {
        font: {
            color: '#3d4c5a'
        },
        tickFormatter: function () {
            return '';
        }
    },
    yaxis: {
        font: {
            color: '#3d4c5a'
        },
        min: 0,
        max: 110
    },
    grid: {
        hoverable: true,
        clickable: true,
        borderWidth: 0,
        color: '#ccc'
    },
    tooltip: true,
    tooltipOpts: {
        content: '%y%',
        defaultTheme: false,
        shifts: {
            x: 0,
            y: 20
        }
    }
};

var plot8 = $.plot($("#" + ChartID), [getData()], options8);

function update() {
    plot8.setData([getData()]);
    plot8.draw();
    setTimeout(update, updateInterval);
};

update();

$(window).resize(function () {
    // redraw the graph in the correctly sized div
    plot8.resize();
    plot8.setupGrid();
    plot8.draw();
});
// * Initialize Realtime Chart