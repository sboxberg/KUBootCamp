// D3 Scatterplot Assignment


  // Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 500;

// Define the chart's margins as an object
var margin = {
  top: 60,
  right: 60,
  bottom: 60,
  left: 60
};

// Define dimensions of the chart area
var chartWidth = svgWidth - margin.left - margin.right;
var chartHeight = svgHeight - margin.top - margin.bottom;

// Select body, append SVG area to it, and set its dimensions
var svg = d3.select("body")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Append a group area, then set its margins
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);


// Load data from csv
d3.csv("./data/data.csv", function (error, healthData) {

  // Throw an error if one occurs
  if (error) throw error;

  // Print the milesData
  console.log(healthData);

  // Format the date and cast values to a number
  healthData.forEach(function (data) {
    data.poorHealth = +data.poorHealth;
    data.foodStamps= +data.foodStamps;
  });

  // Configure a time scale with a range between 0 and the chartWidth
  // Set the domain for the xTimeScale function
  // d3.extent returns the an array containing the min and max values for the property specified
  var xLinearScale = d3.scaleLinear()
    .range([0, chartWidth])
    .domain([0, d3.max(healthData, data => data.foodStamps)])

  // Configure a linear scale with a range between the chartHeight and 0
  // Set the domain for the xLinearScale function
  var yLinearScale = d3.scaleLinear()
    .range([chartHeight, 0])
    .domain([0, d3.max(healthData, data => data.poorHealth)]);

  // Create two new functions passing the scales in as arguments
  // These will be used to create the chart's axes
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  // Configure a drawLine function which will use our scales to plot the line's points
//   var drawLine = d3
//     .line()
//     .x(data => xLinearScale(data.foodStamps))
//     .y(data => yLinearScale(data.poorHealth));
  healthData.forEach(function (data){
    console.log(data.foodStamps);
    console.log(data.poorHealth);
    chartGroup.append("circle")
        .attr("cx",(data.foodStamps*(chartWidth/d3.max(healthData, data => data.foodStamps))))
        .attr("cy",chartHeight - (data.poorHealth*(chartHeight/d3.max(healthData, data => data.poorHealth))))
        .attr("r", 15)
        .attr("stroke","black")
        .attr("fill", "white");
    chartGroup.append("text")
        .attr("dx", (data.foodStamps*(chartWidth/d3.max(healthData, data => data.foodStamps)))-10)
        .attr("dy", chartHeight - (data.poorHealth*(chartHeight/d3.max(healthData, data => data.poorHealth))))
        .text(data.abbr);
    });
    
  // Append an SVG path and plot its points using the line function
//   chartGroup.append("path")
//     // The drawLine function returns the instructions for creating the line for milesData
//     .attr("d", drawLine(healthData))
//     .classed("line", true)

  // Append an SVG group element to the SVG area, create the left axis inside of it
  chartGroup.append("g")
    .classed("axis", true)
    .attr("stroke","white")
    .call(leftAxis);


  // Append an SVG group element to the SVG area, create the bottom axis inside of it
  // Translate the bottom axis to the bottom of the page
  chartGroup.append("g")
    .classed("axis", true)
    .attr("stroke","white")
    .attr("transform", "translate(0, " + chartHeight + ")")
    .call(bottomAxis);

    svg.append("text")             
    .attr("transform",
          "translate(" + (chartWidth/2) + " ," + 
                         (chartHeight + margin.top + 40) + ")")
    .style("text-anchor", "middle")
    .attr("stroke","white")
    .text("Food Stamp Usage");

    // svg.append("text")
    //   .attr("transform", "rotate(-90)")
    //   .attr("y", 0 - margin.left)
    //   .attr("x",0 - (chartHeight / 2))
    //   .attr("dy", "1em")
    //   .attr("stroke","white")
    //   .style("text-anchor", "middle")
    //   .text("Poor Health");  
});