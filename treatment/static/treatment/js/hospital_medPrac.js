function filterAndSearchFunction() {
  var select, search, filter, searchQuery, table, tr, td, i, txtValue;
  select = document.getElementById("departmentFilter");
  search = document.getElementById("doctorSearch");
  filter = select.value.toUpperCase();
  searchQuery = search.value.toUpperCase();
  table = document.getElementById("doctorData");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td");
    if (td) {
      var department = td[3].textContent || td[3].innerText; // Get the department column
      var name = td[0].textContent || td[0].innerText; // Get the name column
      if (department.toUpperCase().indexOf(filter) > -1 && name.toUpperCase().indexOf(searchQuery) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}

function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("doctorTable");
  switching = true;
  dir = "asc";

  while (switching) {
    switching = false;
    rows = table.rows;

    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];

      // Check if both cells have numeric values
      if (!isNaN(parseFloat(x.innerHTML)) && !isNaN(parseFloat(y.innerHTML))) {
        if (dir == "asc") {
          if (parseFloat(x.innerHTML) > parseFloat(y.innerHTML)) {
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          if (parseFloat(x.innerHTML) < parseFloat(y.innerHTML)) {
            shouldSwitch = true;
            break;
          }
        }
      } else {
        // If one or both cells have "N/A", handle the sorting
        if (dir == "asc") {
          if (x.innerHTML === "N/A" && y.innerHTML !== "N/A") {
            shouldSwitch = false;
          } else if (x.innerHTML !== "N/A" && y.innerHTML === "N/A") {
            shouldSwitch = true;
            break;
          } else if (x.innerHTML === "N/A" && y.innerHTML === "N/A") {
            shouldSwitch = false;
          } else if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          if (x.innerHTML === "N/A" && y.innerHTML !== "N/A") {
            shouldSwitch = true;
            break;
          } else if (x.innerHTML !== "N/A" && y.innerHTML === "N/A") {
            shouldSwitch = false;
          } else if (x.innerHTML === "N/A" && y.innerHTML === "N/A") {
            shouldSwitch = false;
          } else if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        }
      }
    }

    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount++;
    } else {
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}