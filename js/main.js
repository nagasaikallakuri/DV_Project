const streamGraphMargin = { top: 20, right: 30, bottom: 0, left: 10 },
  streamGraphWidth = 1100 - streamGraphMargin.left - streamGraphMargin.right,
  streamGraphHeight = 400 - streamGraphMargin.top - streamGraphMargin.bottom;

const barGraphMargin = { top: 20, right: 30, bottom: 0, left: 10 },
  barGraphWidth = 1100 - barGraphMargin.left - barGraphMargin.right,
  barGraphHeight = 500 - barGraphMargin.top - barGraphMargin.bottom;

const clevelandPlotmargin = { top: 30, right: 80, bottom: 50, left: 80 },
  clevelandPlotwidth =
    1100 - clevelandPlotmargin.left - clevelandPlotmargin.right,
  clevelandPlotheight =
    600 - clevelandPlotmargin.top - clevelandPlotmargin.bottom;

const circularBarPlot = { top: 2, right: 0, bottom: 0, left: 2 },
  width = 1100 - circularBarPlot.left - circularBarPlot.right,
  height = 700 - circularBarPlot.top - circularBarPlot.bottom,
  innerRadius = 120,
  outerRadius = Math.min(width, height) / 1.8; // the outerRadius goes from the middle of the SVG area to the border

var streamGraphKeys;
var groupBarKeys;

var streamGraphSvg;
var streamGraphData;

var bubbleGraphSvg;

var interactiveData;

var groupBarGSvg;
var streamTooltip;
var bubbleTooltip;

var clevelandToolTip;

var groupedbarTooltip;
var timeout;

document.addEventListener("DOMContentLoaded", function () {
  //each graph svgs
  streamGraphSvg = d3
    .select("#vis1")
    .append("svg")
    .attr("id", "vis1svg")
    .attr(
      "width",
      streamGraphWidth + streamGraphMargin.left + streamGraphMargin.right + 30
    )
    .attr(
      "height",
      streamGraphHeight + streamGraphMargin.top + streamGraphMargin.bottom + 210
    )
    .append("g")
    .attr(
      "transform",
      `translate(${streamGraphMargin.left}, ${streamGraphMargin.top})`
    );
  bubbleGraphSvg = d3.select("#vis3").append("svg").attr("id", "vis3svg");

  groupBarGSvg = d3
    .select("#vis2")
    .append("svg")
    .attr("id", "vis2svg")
    .attr(
      "width",
      barGraphWidth + barGraphMargin.left + barGraphMargin.right + 50
    )
    .attr(
      "height",
      barGraphHeight + barGraphMargin.top + barGraphMargin.bottom + 190
    )
    .append("g")
    .attr("Height", barGraphHeight)
    .attr(
      "transform",
      `translate(${barGraphMargin.left}, ${barGraphMargin.top})`
    );
  clevelandSvg = d3
    .select("#vis4")
    .append("svg")
    .attr(
      "width",
      clevelandPlotwidth + clevelandPlotmargin.left + clevelandPlotmargin.right
    )
    .attr(
      "height",
      clevelandPlotheight + clevelandPlotmargin.top + clevelandPlotmargin.bottom
    )
    .append("g")
    .attr(
      "transform",
      `translate(${clevelandPlotmargin.left}, ${clevelandPlotmargin.top})`
    );

  circularBarsvg = d3
    .select("#vis5")
    .append("svg")
    .attr("width", width + circularBarPlot.left + circularBarPlot.right)
    .attr("height", height + circularBarPlot.top + circularBarPlot.bottom)
    .append("g")
    .attr(
      "transform",
      `translate(${width / 2 + circularBarPlot.left}, ${
        height / 2 + circularBarPlot.top
      })`
    );

  // create a tooltip
  circularBarTooltip = d3
    .select("#circulaBarTooltip")
    .append("div")
    .style("position", "absolute")
    .style("visibility", "hidden")
    .style("background-color", "white")
    .style("z-index", "10")
    .style("border", "solid")
    .style("border-width", "1px")
    .style("border-radius", "5px")
    .style("padding", "10px")
    .html(
      `<div>
        <div>Country: Iran</div>
        <div>Average Life Span: </div>
        <div>Percentage of Death: </div>
        </div>`
    );
  Promise.all([
    d3.csv("merged_data/StreamgraphData.csv"),
    d3.csv("merged_data/GroupedBarChart.csv"),
    d3.csv("merged_data/BubbleChartData.csv"),
    d3.csv("merged_data/BubbleGraphAlgoDataPreProcessed.csv"),
    d3.csv("./data/ClevelandPlotData.csv"),
    d3.csv("./data/CircularBarPlotData.csv"),
  ]).then(function (values) {
    //dataset of all graph values
    streamGraphKeys = values[0].columns.slice(1);
    streamGraphData = values[0];
    groupBarKeys = values[1].columns.slice(1);
    groupedBarData = values[1];
    bubbleChartData = values[2];
    interactiveData = values[3];
    deaths = values[4];
    lifespan = values[5];
    drawGraphs();
  });
  groupedbarTooltip = d3.select(".toolTip");
  bubbleTooltip = d3.select("#vis3tooltip");
  streamTooltip = d3
    .select("#vis1_tooltip")
    .style("background", "white")
    .style("opacity", 0);
  clevelandToolTip = d3
    .select("#cleveland3tooltip")
    .append("div")
    .style("position", "absolute")
    .style("visibility", "hidden")
    .style("background-color", "white")
    .style("z-index", "10")
    .style("border", "solid")
    .style("border-width", "1px")
    .style("border-radius", "5px")
    .style("padding", "10px")
    .html(
      `<div>
      <div>Country: Iran</div>
      <div>No of Male Death: </div>
      <div>No of Female Death: </div>
      </div>`
    );
});
//function for all the graphs
function drawGraphs() {
  drawStreamGraph();
  drawBubbleGraph();
  drawGroupBarGraph();
  drawClevelandGraph();
  drawCircularBarGraph();
}
//preprocessing the stream graph data
function drawStreamGraph() {
  var country = d3.select("#countries option:checked").node().value;
  var survival = d3.select("#survival option:checked").node().value;
  drawSGraph(country, survival);
}
//plotting the stream graph
function drawSGraph(country, survival) {
  streamGraphSvg.selectAll("*").remove();
  var flag = survival == "Hosp";
  var deadkeys = ["DATE"];
  var hospkeys = ["DATE"];
  var date = streamGraphData.map((d) => new Date(d.DATE));
  for (var i = 1; i < streamGraphKeys.length; i++) {
    if (i % 2 == 0) deadkeys.push(streamGraphKeys[i]);
    else hospkeys.push(streamGraphKeys[i]);
  }
  var xScale = d3
    .scaleTime()
    .domain(
      d3.extent(date, function (d) {
        return new Date(d);
      })
    )
    .range([0, streamGraphWidth]);
  var xAxis = d3.axisBottom(xScale);
  const hospkeysdata = streamGraphData.map(function (d) {
    const res = [];
    hospkeys.forEach((e) => {
      if (e != "DATE") res[e] = +d[e];
      else res[e] = new Date(d[e]);
    });
    return res;
  });
  const deadkeysdata = streamGraphData.map(function (d) {
    const res = [];
    deadkeys.forEach((e) => {
      if (e != "DATE") res[e] = +d[e];
      else res[e] = new Date(d[e]);
    });
    return res;
  });
  streamGraphSvg
    .append("g")
    .attr("transform", "translate(50," + streamGraphHeight * 1.48 + ")")
    .call(xAxis);
  var yScale = d3
    .scaleLinear()
    .domain([0, flag ? 315000 : 18000])
    .range([streamGraphHeight * 1.35, 0]);
  var yAxis = d3.axisLeft(yScale);
  streamGraphSvg
    .append("g")
    .attr("transform", "translate(50," + streamGraphHeight / 7.7 + ")")
    .call(yAxis);

  const color = d3
    .scaleOrdinal()
    .domain(
      flag
        ? hospkeys.filter(function (e) {
            return e != "DATE";
          })
        : deadkeys.filter(function (e) {
            return e != "DATE";
          })
    )
    .range([
      "#1f77b4",
      "#ff7f0e",
      "#2ca02c",
      "#d62728",
      "#9467bd",
      "#8c564b",
      "#e377c2",
      "#7f7f7f",
      "#bcbd22",
      "#17becf",
      "#4B0082",
    ]);
  const stackedData = d3
    .stack()
    .offset(d3.stackOffsetZero)
    .keys(
      flag
        ? hospkeys.filter(function (e) {
            return e != "DATE";
          })
        : deadkeys.filter(function (e) {
            return e != "DATE";
          })
    )(flag ? hospkeysdata : deadkeysdata);
  var mouseover = function (d) {
    if (country == "All") {
      d3.selectAll(".myArea").style("opacity", 0.2);
      d3.select(this).style("stroke", "black").style("opacity", 1);
    } else {
      if (d3.select(this).attr("id") == country) {
        // Tooltip.style("opacity", 1);
      }
    }
  };
  var mouseleave = function (d) {
    // Tooltip.style("opacity", 0);
    // drawGBgraph(country);
    // drawBGraph(country, survival);
    // if (country == "All") {
    //   d3.selectAll(".myArea").style("opacity", 1).style("stroke", "none");
    // }
  };

  const area = d3
    .area()
    .x(function (d) {
      return xScale(d.data["DATE"]);
    })
    .y0(function (d) {
      return yScale(d[0]);
    })
    .y1(function (d) {
      return yScale(d[1]);
    });
  streamGraphSvg
    .selectAll("mylayers")
    .data(stackedData)
    .enter()
    .append("path")
    .attr("class", "myArea")
    .attr("id", function (d) {
      var t = d.key.split("_");
      return t[0];
    })
    .style("fill", function (d) {
      return color(d.key);
    })
    .style(
      "opacity",
      country == "All"
        ? 1
        : function (d) {
            if (d3.select(this).attr("id") == country) return 1;
            return 0.2;
          }
    )
    .attr("transform", "translate(50,50)")
    .attr("d", area)

    .on("click", function (d, i) {
      var c = d3.select(this).attr("id");
      drawGBgraph(c);
      drawBGraph(c, survival);
      drawClevelandgraph(c);
      drawCircularBarandGraph(c);

      if (country == "All") {
        d3.selectAll(".myArea").style("opacity", 0.2);
        d3.select(this).style("stroke", "black").style("opacity", 1);
      } else {
        if (d3.select(this).attr("id") == country) {
          // Tooltip.style("opacity", 1);
        }
      }
    })
    .on("mouseover", function (d, i) {
      var c = d3.select(this).attr("id");
      streamTooltip
        .style("left", d.pageX + 20 + "px")
        .style("top", d.pageY - 15 + "px")
        .style("background", "white")
        .style("position", "absolute")
        .style("display", "inline")
        .style("opacity", 1)
        .html("Country: " + c);
    })
    .on("mouseleave", mouseleave)
    .on("mouseout", function (d, i) {
      streamTooltip.style("display", "none");
    });
  streamGraphSvg
    .append("text")
    .attr("text-anchor", "end")
    .attr("y", 4)
    .attr("x", barGraphMargin.top - 300)
    .attr("transform", "rotate(-90)")
    .text("PATIENT COUNT");
  // streamGraphSvg
  //   .append("text")
  //   .attr("text-anchor", "end")
  //   .attr("x", 400)
  //   .attr("y", barGraphHeight + barGraphMargin.top + 130)
  //   .text("DATE");
}
function drawGroupBarGraph() {
  var country = d3.select("#countries option:checked").node().value;

  drawGBgraph(country);
}
function drawGBgraph(country) {
  groupBarGSvg.selectAll("*").remove();
  var groups = groupedBarData.map((d) => d.AGE_GROUP);
  hospkeys = [];
  deadkeys = [];
  recoveredkeys = [];
  groupBarKeys.map(function (k, i) {
    if (i % 3 == 1) {
      hospkeys.push(k);
    } else if (i % 3 == 2) {
      deadkeys.push(k);
    } else {
      recoveredkeys.push(k);
    }
  });

  var subgroups = [
    country + "_Hosp",
    country + "_Recovered",
    country + "_Dead",
  ];
  var x = d3
    .scaleBand()
    .domain(groups)
    .range([0, barGraphWidth])
    .padding([0.2]);
  var maxDomain = 0;
  var finaldata = groupedBarData.map(function (d) {
    var res = {};
    res["AGE_GROUP"] = d.AGE_GROUP;
    subgroups.map(function (t) {
      res[t] = +d[t];
      maxDomain = Math.max(maxDomain, res[t]);
    });
    return res;
  });
  var xAxis = d3.axisBottom(x);

  groupBarGSvg
    .append("g")
    .attr("transform", "translate(70," + barGraphHeight * 1.21 + ")")
    .call(xAxis);

  var xSubgroup = d3
    .scaleBand()
    .domain(subgroups)
    .range([0, x.bandwidth()])
    .padding([0.05]);

  var color = d3
    .scaleOrdinal()
    .domain(subgroups)
    .range(["#87CEFA", "#32CD32", "#FF5E5E"]);
  var y = d3
    .scaleLinear()
    .domain([0, Math.ceil(maxDomain)])
    .range([barGraphHeight, 0]);

  var yAxis = d3.axisLeft(y);

  groupBarGSvg.append("g").attr("transform", "translate(70,101)").call(yAxis);

  groupBarGSvg
    .append("g")
    .attr("transform", "translate(70,100)")
    .selectAll("g")
    .data(finaldata)
    .enter()
    .append("g")
    .attr("transform", function (d) {
      return "translate(" + x(d.AGE_GROUP) + ",0)";
    })
    .selectAll("rect")
    .data(function (d) {
      return subgroups.map(function (key) {
        return { key: key, value: d[key] };
      });
    })
    .enter()
    .append("rect")
    .attr("x", function (d) {
      return xSubgroup(d.key);
    })
    .attr("y", function (d) {
      return y(d.value);
    })
    .attr("width", xSubgroup.bandwidth())
    .attr("height", function (d) {
      return barGraphHeight - y(d.value);
    })
    .attr("fill", function (d) {
      return color(d.key);
    })
    .on("mousemove", function (d, val) {
      if (timeout) clearTimeout(timeout);
      var t = val.key.replace("_", " ");
      groupedbarTooltip
        .style("top", d.pageY + "px")
        .style("left", d.pageX + "px")
        .style("display", "inline-block")
        .html(val.key.replace("_", " ") + " : " + val.value);
    })
    .on("mouseout", function (d) {
      if (timeout) clearTimeout(timeout);
      timeout = setTimeout(function () {
        groupedbarTooltip.style("display", "none");
      }, 500);
    });

  groupBarGSvg
    .append("text")
    .attr("text-anchor", "end")
    .attr("x", 600)
    .attr("y", barGraphHeight + barGraphMargin.top + 130)
    .text("AGE GROUPS");

  groupBarGSvg
    .append("text")
    .attr("text-anchor", "end")
    .attr("y", 10)
    .attr("x", barGraphMargin.top - 300)
    .attr("transform", "rotate(-90)")
    .text("PATIENT COUNT");

  var size = 20;

  groupBarGSvg
    .selectAll("mydots")
    .data(subgroups)
    .enter()
    .append("rect")
    .attr("x", 900)
    .attr("y", function (d, i) {
      return 50 + i * (size + 10);
    })
    .attr("width", size)
    .attr("height", size)
    .style("fill", function (d) {
      return color(d);
    });

  groupBarGSvg
    .selectAll("mylabels")
    .data(subgroups)
    .enter()
    .append("text")
    .attr("x", 910 + size * 1.2)
    .attr("y", function (d, i) {
      return 50 + i * (size + 10) + size / 2;
    })
    .style("fill", function (d) {
      return color(d);
    })
    .text(function (d) {
      return d.replace("_", " ");
    })
    .attr("text-anchor", "left")
    .style("alignment-baseline", "middle");
}
function drawBubbleGraph() {
  var country = d3.select("#countries option:checked").node().value;
  var survival = d3.select("#survival option:checked").node().value;
  drawBGraph(country, survival);
}
function drawBGraph(country, survival) {
  bubbleGraphSvg.selectAll("*").remove();
  var selectedValue = country + "_" + survival;
  var bubbleFinalData = [];
  bubbleFinalData = bubbleChartData.map(function (d) {
    res = {};
    res.Syndrome = d.Syndrome;
    res.value = +d[selectedValue];
    return res;
  });

  var fiteredInteractiveData = interactiveData.map(function (d) {
    var res = {};
    res[d.Syndrome] = d[selectedValue];
    return res;
  });
  console.log(fiteredInteractiveData);
  var finaldataset = { children: bubbleFinalData };
  var diameter = 680;
  var color = d3.scaleOrdinal(d3.schemeTableau10);
  var bubble = d3.pack(bubbleFinalData).size([diameter, diameter]).padding(5.5);
  var nodes = d3.hierarchy(finaldataset).sum((d) => d.value);

  bubbleGraphSvg
    .attr("width", diameter + 440)
    .attr("height", diameter - 20)
    .attr("class", "bubble")
    .style("margin-left", 15 + "vw");

  var node = bubbleGraphSvg
    .selectAll(".node")
    .data(bubble(nodes).descendants())
    .enter()
    .filter(function (d) {
      return !d.children;
    })
    .append("g")
    .attr("class", "node")
    .attr("id", function (d) {
      return d.data.Syndrome;
    })
    .on("mouseover", function mousemove(d, i) {
      if (timeout) clearTimeout(timeout);
      bubbleTooltip
        .html(
          "Syndrome: " +
            i.data.Syndrome +
            "<br> " +
            "Patient Count: " +
            i.data.value
        )
        .style("top", d.pageY + "px")
        .style("left", d.pageX + "px")
        .style("display", "inline-block");
      // .style('visibility', 'visible')

      // d3.select(this).style('stroke', '#C0C0C0');
    })
    .on("mousemove", (e) =>
      bubbleTooltip
        .style("top", `${e.pageY}px`)
        .style("left", `${e.pageX + 10}px`)
    )
    .on("click", function (d, i) {
      console.log(i);
      var selection = fiteredInteractiveData.find(function (e, j) {
        if (Object.keys(e)[0] == i.data.Syndrome) return e[Object.keys(e)[0]];
      });
      console.log(selection);

      d3.selectAll(".node").each(function (e) {
        if (
          e.data.Syndrome == selection[i.data.Syndrome] ||
          e.data.Syndrome == i.data.Syndrome
        ) {
          d3.select(this).style("opacity", 1).transition();
          console.log(fiteredInteractiveData[i.data.Syndrome]);
        } else d3.select(this).style("opacity", 0.2);
      });

      // d3.select(this).style("stroke", "black").style("opacity", 1);
      // d3.select().style("stroke", "black").style("opacity", 1);
    })
    .on("mouseleave", function (d) {
      bubbleTooltip.style("display", "none");
    })
    .attr("transform", function (d) {
      return "translate(" + d.x + "," + d.y + ")";
    });
  node.append("title").text(function (d) {
    return d.data.Syndrome + ": " + d.value;
  });

  node
    .append("circle")
    .attr("r", function (d) {
      return d.r;
    })
    .style("fill", function (d, i) {
      return color(i);
    });
  node
    .append("text")
    .attr("dy", ".2em")
    .style("text-anchor", "middle")
    .text(function (d) {
      return d.data.Syndrome.substring(0, d.r / 3);
    })
    .attr("font-family", "sans-serif")
    .attr("font-size", function (d) {
      return d.r / 4;
    })
    .attr("fill", "white");

  // d3.select(self.frameElement).style("height", diameter + "px");
}

function drawClevelandGraph() {
  var country = d3.select("#countries option:checked").node().value;

  drawClevelandgraph(country);
}

function drawClevelandgraph(country) {
  let range = [0, 0];

  let highestRange;

  highestRange = Math.max.apply(
    Math,
    deaths.map(function (o) {
      return o.male;
    })
  );

  deaths.forEach((deathsByGender) => {
    if (deathsByGender.male > range[1] || deathsByGender.female > range[1]) {
      if (deathsByGender.male > deathsByGender.female) {
        range[1] = deathsByGender.male;
      } else {
        range[1] = deathsByGender.female;
      }
    }
    if (deathsByGender.male < range[0] || deathsByGender.female < range[0]) {
      if (deathsByGender.male < deathsByGender.female) {
        range[0] = deathsByGender.male;
      } else {
        range[0] = deathsByGender.female;
      }
    }
  });

  // Add X axis

  const x = d3
    .scaleLinear()
    .domain([range[0], highestRange])
    .range([0, clevelandPlotwidth]);
  clevelandSvg
    .append("g")
    .attr("transform", `translate(0, ${clevelandPlotheight})`)
    .call(d3.axisBottom(x));

  // Y axis

  const y = d3
    .scaleBand()
    .range([0, clevelandPlotheight])
    .domain(
      deaths.map(function (d) {
        return d.country;
      })
    )
    .padding(1);
  clevelandSvg.append("g").call(d3.axisLeft(y));

  // Lines
  clevelandSvg
    .selectAll("myline")
    .data(deaths)
    .join("line")
    .attr("x1", function (d) {
      return x(parseInt(d.male));
    })
    .attr("x2", function (d) {
      return x(parseInt(d.female));
    })
    .attr("y1", function (d) {
      return y(d.country);
    })
    .attr("y2", function (d) {
      return y(d.country);
    })
    .attr("stroke", "black")
    .attr("stroke-width", "5px")
    .style(
      "stroke",
      country == "All"
        ? "black"
        : function (d) {
            if (d.country == country) {
              return "black";
            }
            return "#BEC0C1";
          }
    );

  // Circles of variable 1
  clevelandSvg
    .selectAll("mycircle")
    .data(deaths)
    .join("circle")
    .attr("cx", function (d) {
      // console.log(parseInt(d.male));
      return x(parseInt(d.male));
    })
    .attr("cy", function (d) {
      return y(d.country);
    })
    .attr("r", "12")
    .on("mouseover", function (d, i) {
      // console.log( i);
      return clevelandToolTip.style("visibility", "visible").html(
        `<div>
    <div>Country: ${i.Country}</div>
    <div>No of Male Death:${i.male} </div>
    <div>No of Female Death:${i.female}  </div>
    </div>`
      );
    })
    .on("mouseover", function (d, i) {
      //console.log(i);
      return clevelandToolTip.style("visibility", "visible").html(
        `<div>
    <div>Country: ${i.Country}</div>
    <div>No of Male Death:${i.male} </div>
    <div>No of Female Death:${i.female}  </div>
    </div>`
      );
    })
    .on("mousemove", function (d, i) {
      //console.log(i);
      return clevelandToolTip
        .style("top", event.pageY - 50 + "px")
        .style("left", event.pageX + 50 + "px")
        .html(
          `<div>
    <div>Country: ${i.country}</div>
    <div>No of Male Death:${i.male} </div>
    <div>No of Female Death:${i.female}  </div>

    </div>`
        );
    })
    .on("mouseout", function () {
      return clevelandToolTip.style("visibility", "hidden");
    })
    .style("fill", "#1909DF")
    .style(
      "fill",
      country == "All"
        ? "#1909DF"
        : function (d) {
            if (d.country == country) {
              return "#1909DF";
            }
            return "#C2CDF4";
          }
    );

  // Circles of variable 2
  clevelandSvg
    .selectAll("mycircle")
    .data(deaths)
    .join("circle")
    .attr("cx", function (d) {
      return x(parseInt(d.female));
    })
    .attr("cy", function (d) {
      return y(d.country);
    })
    .attr("r", "12")
    .on("mouseover", function (d, i) {
      console.log("", i);
      return clevelandToolTip.style("visibility", "visible").html(
        `<div>
          <div>Country: ${i.country}</div>
    <div>No of Male Death:${i.male} </div>
    <div>No of Female Death:${i.female}  </div>
    </div>`
      );
    })
    .on("mouseover", function (d, i) {
      //console.log(i);
      return clevelandToolTip.style("visibility", "visible").html(
        `<div>
          <div>Country: ${i.country}</div>
    <div>No of Male Death:${i.male} </div>
    <div>No of Female Death:${i.female}  </div>
    </div>`
      );
    })
    .on("mousemove", function (d, i) {
      //console.log(i);
      return clevelandToolTip
        .style("top", event.pageY - 50 + "px")
        .style("left", event.pageX + 50 + "px")
        .html(
          `<div>
            <div>Country: ${i.country}</div>
    <div>No of Male Death:${i.male} </div>
    <div>No of Female Death:${i.female}  </div>
    </div>`
        );
    })
    .on("mouseout", function () {
      return clevelandToolTip.style("visibility", "hidden");
    })
    .style("fill", "#e6099c")
    .style(
      "fill",
      country == "All"
        ? "#e6099c"
        : function (d) {
            if (d.country == country) {
              return "#e6099c";
            }
            return "#eda6d5";
          }
    );
  clevelandSvg
    .append("rect")
    .attr("x", 740)
    .attr("y", 10)
    .attr("width", 15)
    .attr("height", 15)
    .attr("fill", "#1909df");

  clevelandSvg
    .append("rect")
    .attr("x", 740)
    .attr("y", 30)
    .attr("width", 15)
    .attr("height", 15)
    .attr("fill", "#e6099c");

  clevelandSvg
    .append("text")
    .attr("x", 770)
    .attr("y", 20)
    .text("Number of Male Deaths")
    .style("font-size", "20px")
    .attr("alignment-baseline", "middle");

  clevelandSvg
    .append("text")
    .attr("x", 770)
    .attr("y", 40)
    .text("Number of Female Deaths")
    .style("font-size", "20px")
    .attr("alignment-baseline", "middle");

  clevelandSvg
    .append("text")
    .attr("class", "axis-label")
    .attr("text-anchor", "middle")
    .attr("x", clevelandPlotwidth / 2)
    .attr("y", clevelandPlotheight + 33)
    .attr("font-weight", 700)
    .text("Total Number of Deaths");

  clevelandSvg
    .append("text")
    .attr("class", "axis-label")
    .attr("transform", "rotate(-90)")
    .attr("y", "-63px")
    .attr("x", -clevelandPlotheight / 2)
    .attr("text-anchor", "middle")
    .attr("font-weight", 700)
    .text("Places");
}

function drawCircularBarGraph() {
  var country = d3.select("#countries option:checked").node().value;

  drawCircularBarandGraph(country);
}

function drawCircularBarandGraph(country) {
  let range = [0, 0];
  const x = d3
    .scaleBand()
    .range([0, 2 * Math.PI]) // X axis goes from 0 to 2pi = all around the circle. If I stop at 1Pi, it will be around a half circle
    .align(0)
    .domain(lifespan.map((d) => d.Country)); // The domain of the X axis is the list of states.

  // Y scale outer variable
  const y = d3
    .scaleRadial()
    .range([innerRadius, outerRadius]) // Domain will be define later.
    .domain([0, 50]); // Domain of Y is from 0 to the max seen in the data

  // Second barplot Scales
  const ybis = d3
    .scaleRadial()
    .range([innerRadius, 2]) // Domain will be defined later.
    .domain([0, 3.54]);

  // Add the bars
  circularBarsvg
    .append("g")
    .selectAll("path")
    .data(lifespan)
    .join("path")
    .attr("fill", "#69b3a2")
    .attr("class", "yo")
    .attr(
      "d",
      d3
        .arc() // imagine your doing a part of a donut plot
        .innerRadius(innerRadius)
        .outerRadius((d) => y(d.averageLifeSpan))
        .startAngle((d) => x(d.Country))
        .endAngle((d) => x(d.Country) + x.bandwidth())
        .padAngle(0.03)
        .padRadius(innerRadius)
    )
    .on("mouseover", function (d, i) {
      console.log(i);
      return circularBarTooltip.style("visibility", "visible").html(
        `<div>
    <div>Country: ${i.Country}</div>
    <div>Average Life Span: ${i.averageLifeSpan}</div>
    <div>Percentage of Death: ${i.percentageOfDeath}</div>
    </div>`
      );
    })
    .on("mousemove", function (d, i) {
      console.log(i);
      return circularBarTooltip
        .style("top", event.pageY - 50 + "px")
        .style("left", event.pageX + 50 + "px")
        .html(
          `<div>
    <div>Country: ${i.Country}</div>
    <div>Average Life Span: ${i.averageLifeSpan}</div>
    <div>Percentage of Death: ${i.percentageOfDeath}</div>
    </div>`
        );
    })
    .on("mouseout", function () {
      return circularBarTooltip.style("visibility", "hidden");
    })
    .style(
      "fill",
      country == "All"
        ? "#69b3a2"
        : function (d) {
            console.log(d.Country, "====================", country);
            if (d.Country == country) {
              console.log(d.Country);
              return "#69b3a2";
            }
            return "#D6F2EB";
          }
    );

  // Add the labels
  circularBarsvg
    .append("g")
    .selectAll("g")
    .data(lifespan)
    .join("g")
    .attr("text-anchor", function (d) {
      return (x(d.Country) + x.bandwidth() / 2 + Math.PI) % (2 * Math.PI) <
        Math.PI
        ? "end"
        : "start";
    })
    .attr("transform", function (d) {
      return (
        "rotate(" +
        (((x(d.Country) + x.bandwidth() / 2) * 180) / Math.PI - 90) +
        ")" +
        "translate(" +
        (y(d.averageLifeSpan) + 10) +
        ",0)"
      );
    })
    .append("text")
    .text((d) => d.Country)
    .attr("transform", function (d) {
      return (x(d.Country) + x.bandwidth() / 2 + Math.PI) % (2 * Math.PI) <
        Math.PI
        ? "rotate(180)"
        : "rotate(0)";
    })
    .style("font-size", "11px")
    .attr("alignment-baseline", "middle");

  circularBarsvg
    .append("circle")
    .attr("cx", 390)
    .attr("cy", 100)
    .attr("r", 8)
    .style("fill", "#69b3a2");

  circularBarsvg
    .append("circle")
    .attr("cx", 390)
    .attr("cy", 140)
    .attr("r", 8)
    .style("fill", "red");

  circularBarsvg
    .append("text")
    .attr("x", 410)
    .attr("y", 105)
    .text("Average Life Span")
    .style("font-size", "14px");

  circularBarsvg
    .append("text")
    .attr("x", 410)
    .attr("y", 145)
    .text("Percentage of Deaths")
    .style("font-size", "14px");

  // Add the second series
  circularBarsvg
    .append("g")
    .selectAll("path")
    .data(lifespan)
    .join("path")
    .attr("fill", "red")
    .attr(
      "d",
      d3
        .arc() // imagine your doing a part of a donut plot
        .innerRadius((d) => ybis(0))
        .outerRadius((d) => ybis(d.percentageOfDeath))
        .startAngle((d) => x(d.Country))
        .endAngle((d) => x(d.Country) + x.bandwidth())
        .padAngle(0.01)
        .padRadius(innerRadius)
    )
    .on("mouseover", function (d, i) {
      console.log(i);
      return circularBarTooltip.style("visibility", "visible").html(
        `<div>
    <div>Country: ${i.Country}</div>
    <div>Average Life Span: ${i.averageLifeSpan}</div>
    <div>Percentage of Death: ${i.percentageOfDeath}</div>
    </div>`
      );
    })
    .on("mousemove", function (d, i) {
      console.log(i);
      return circularBarTooltip
        .style("top", event.pageY - 50 + "px")
        .style("left", event.pageX + 50 + "px")
        .html(
          `<div>
    <div>Country: ${i.Country}</div>
    <div>Average Life Span: ${i.averageLifeSpan}</div>
    <div>Percentage of Death: ${i.percentageOfDeath}</div>
    </div>`
        );
    })
    .on("mouseout", function () {
      return circularBarTooltip.style("visibility", "hidden");
    })
    .style(
      "fill",
      country == "All"
        ? "red"
        : function (d) {
            console.log(d.Country, "====================", country);
            if (d.Country == country) {
              console.log(d.Country);
              return "red";
            }
            return "#F9CE91";
          }
    );
}
