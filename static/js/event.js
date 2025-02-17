$(document).ready(function() {
  fetch('/jsd')
    .then(response => response.json())
    .then(data => {
      const all_temperatures_first = data.all_temperatures_first;
      const all_temperatures_second = data.all_temperatures_second;
      const all_dates_first = data.all_dates_first;
      const all_dates_second = data.all_dates_second;

      console.log(all_temperatures_first);
      console.log(all_temperatures_second);
      console.log(all_dates_first);
      console.log(all_dates_second);

      // 有效陣列並且不為空
      if (Array.isArray(all_dates_first) && all_dates_first.length > 0 && Array.isArray(all_temperatures_first) && all_temperatures_first.length > 0
          && Array.isArray(all_dates_second) && all_dates_second.length == 0 && Array.isArray(all_temperatures_second) && all_temperatures_second.length == 0) {
        // 初始化DataTable並使用資料填充表格
        console.log(" in if");
        $('#myTable').DataTable({
          data : all_dates_first.map((value, index) => [value, all_temperatures_first[index]]),
          columns: [
            { title: 'dates' },
            { title: 'temperatures' }
          ]
        });
      } else {
        console.log(" in else");
        $('#myTable').DataTable().destroy();
        $('#myTable').DataTable({
          data: all_dates_second && all_temperatures_second ? all_dates_second.map((value, index) => [value, all_temperatures_second[index]]) : [],
          columns: [
            { title: 'dates' },
            { title: 'temperatures' }
          ]
        });
      }
    });
});
