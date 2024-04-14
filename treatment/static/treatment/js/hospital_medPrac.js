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