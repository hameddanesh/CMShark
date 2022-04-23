var intravlHistory = Array(),
        last = Array();

function loadCsv() {
    let startRow = 0;
    if ($("#hasHeader").prop("checked") === true) {
        startRow = 1;
    }
    csv = new FileReader();
    csv.onload = function (e) {
        let rows = e.target.result.split("\n");

        for (let i = startRow; i < rows.length; i++) {
            let columns = rows[i].split(",");
            if (columns[6] === '"Application Data"') {
                searchLast(columns);
            }
        }
        console.log(intravlHistory);
        download_csv(intravlHistory);
    };
    csv.readAsText($("#input-csv")[0].files[0]);
}

function searchLast(column) {
    /*if (last.length !== 0) {
     let found = false;
     for (let i = 0; i < last.length; i++) {
     if (
     column[2] === last[i][2] &&
     column[3] === last[i][3] &&
     column[4] === last[i][4] &&
     column[6] === last[i][6]
     ) {*/
    //console.log(column[1] + "  TO  " + last[i][1] + "   " + (StringToSysTime(column[1]) - StringToSysTime(last[i][1])));
    //let timeDif = StringToSysTime(column[1]) - StringToSysTime(last[i][1]);

    let flowType = "out";
    if (column[2] !== '\"192.168.1.105\"')
    {
        flowType = "in";
    }
    //if (flowType === "in") {
    intravlHistory[intravlHistory.length] = [
        column[1],
        column[2],
        column[3],
        column[4],
        column[6],
        flowType
    ];
    // }
    /*last[i] = column;
     found = true;
     break;
     }
     }
     
     if (!found) {
     last[last.length] = column;
     }
     } else {
     last[last.length] = column;
     }*/
}

function StringToSysTime(timeString) {
    let timeparts = timeString.split(":");
    return (
            parseInt(timeparts[0].replace('"', "")) * 3600 +
            parseInt(timeparts[1].replace('"', "")) * 60 +
            parseFloat(timeparts[2].replace('"', ""))
            );
}

function download_csv(data) {
    var csv = '\"Time Dif\","\Source\",\"Destination\",\"Protocol\",\"Type\"\n';
    for (let i = 0; i < data.length; i++) {
        csv += data[i].join(",") + "\n";
    }

    console.log(csv);
    var hiddenElement = document.createElement("a");
    hiddenElement.href = "data:text/csv;charset=utf-8," + encodeURI(csv);
    hiddenElement.target = "_blank";
    hiddenElement.download = "output.csv";
    hiddenElement.click();
}
