$(function() {
 google.charts.load('upcoming', {'packages':['geochart']});
  google.charts.setOnLoadCallback(drawRegionsMap);
  function drawRegionsMap() {
	"use strict";
    var data = google.visualization.arrayToDataTable([
	  ['Country', 'Visitors'],
	  ['Germany', 200],
	  ['America', 600],
	  ['Brazil', 100],
	  ['Canada', 400],
	  ['France', 190],
	  ['RU', 210]
	]);
	var options = {};
	var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));
	chart.draw(data, options);
		
// Initialize Line Chart
		var data1 = [{
			data: [[1,5.3],[2,5.9],[3,7.2],[4,8],[5,7],[6,6.5],[7,6.2],[8,6.7],[9,7.2],[10,7],[11,6.8],[12,7]],
			label: 'Sales',
			points: {
				show: true,
				radius: 6
			},
			splines: {
				show: true,
				tension: 0.45,
				lineWidth: 5,
				fill: 0
			}
		}, {
			data: [[1,6.6],[2,7.4],[3,8.6],[4,9.4],[5,8.3],[6,7.9],[7,7.2],[8,7.7],[9,8.9],[10,8.4],[11,8],[12,8.3]],
			label: 'Orders',
			points: {
				show: true,
				radius: 6
			},
			splines: {
				show: true,
				tension: 0.45,
				lineWidth: 4,
				fill: 0
			}
		}];

		var options1 = {
			colors: ['#f7bb97', '#dd5e89'],
			series: {
				shadowSize: 0
			},
			xaxis:{
				font: {
					color: '#3d4c5a'
				},
				position: 'bottom',
				ticks: [
					[ 1, 'Jan' ], [ 2, 'Feb' ], [ 3, 'Mar' ], [ 4, 'Apr' ], [ 5, 'May' ], [ 6, 'Jun' ], [ 7, 'Jul' ], [ 8, 'Aug' ], [ 9, 'Sep' ], [ 10, 'Oct' ], [ 11, 'Nov' ], [ 12, 'Dec' ]
				]
			},
			yaxis: {
				font: {
					color: '#3d4c5a'
				}
			},
			grid: {
				hoverable: true,
				clickable: true,
				borderWidth: 0,
				color: '#ccc'
			},
			tooltip: true,
			tooltipOpts: {
				content: '%s: %y.4',
				defaultTheme: false,
				shifts: {
					x: 0,
					y: 20
				}
			}
		};

		var plot1 = $.plot($("#line-chart"), data1, options1);

		$(window).resize(function() {
			// redraw the graph in the correctly sized div
			plot1.resize();
			plot1.setupGrid();
			plot1.draw();
		});
		// * Initialize Line Chart
  }

  var graph = new Rickshaw.Graph({
	element: document.querySelector("#rickshaw"),
	renderer: 'area',
	series: [{
		name: 'Series 1',
		color: 'steelblue',
		data: [{ x: 0, y: 23 }, { x: 1, y: 15 }, { x: 2, y: 79 }, { x: 3, y: 31 }, { x: 4, y: 60 }]
	}, {
		name: 'Series 2',
		color: 'lightblue',
		data: [{ x: 0, y: 30 }, { x: 1, y: 20 }, { x: 2, y: 64 }, { x: 3, y: 50 }, { x: 4, y: 15 }]
	}]
});
graph.render();
});


// Initialize Combined Chart
var data5 = [{
	data: [[1, 12], [2, 12], [3, 14], [4, 16], [5, 16], [6, 17], [7, 15], [8, 11], [9, 13], [10, 11], [11, 15], [12, 14]],
	label: 'Sales Report',
	points: {
		show: true,
		radius: 3
	},
	splines: {
		show: true,
		tension: 0.45,
		lineWidth: 3,
		fill: 0
	}
}, {
	data: [[1, 9], [2, 13], [3, 8], [4, 9], [5, 18], [6, 14], [7, 13], [8, 10], [9, 12], [10, 18], [11, 9], [12, 17]],
	label: 'Annual Revenue',
	bars: {
		show: true,
		barWidth: 0.4,
		lineWidth: 0,
		fillColor: { colors: [{ opacity: 0.6 }, { opacity: 0.8 }] }
	}
}];

var options5 = {
	colors: ['#ffdc88', '#a169c9'],
	series: {
		shadowSize: 0
	},
	xaxis: {
		font: {
			color: '#3d4c5a'
		}
	},
	yaxis: {
		font: {
			color: '#3d4c5a'
		}
	},
	grid: {
		hoverable: true,
		clickable: true,
		borderWidth: 0,
		color: '#ccc'
	},
	tooltip: true,
	tooltipOpts: { content: '%s of %x.1 is %y.4', defaultTheme: false, shifts: { x: 0, y: 20 } }
};

var plot5 = $.plot($("#combined-chart"), data5, options5);