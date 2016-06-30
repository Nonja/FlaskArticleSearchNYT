$(function(){
  $("#submitform").submit(function(e) {
    var page = 0;
    implementsearch(e, page);
  })
  $("#loadmore").submit(function(e){
    var page = $("#page").html();
    implementsearch(e, page);
    })
});

function implementsearch(event, p) {
      event.preventDefault();
      var query = $("#searchquery").val();
      page = p;
      $.ajax({
          type: 'GET',
          url: '/searchrequest',
          data: { searchrequest : $("#searchquery").val(),
                  begindate : $("#begindate").val(),
                  enddate : $("#enddate").val(),
                  page : page },
          success: function(response) {
              console.log(response);
              $("#resultlist").append("<ul id='list'></ul>");    
                $.each(response.news, function(head, url) {
                  $("#list").append('<li>' + head + '   ' + '<a href=' + url + '>' + url + '</a></li><br>');
                })
                $("#resultcount").html('<p>Found ' + response.results + ' results.</p>');
                $("#resultpages").html("Page " + "<p id='page'>" + response.page + "</p> / " + response.totalpages);
          },
          error: function(error) {
              console.log(error);
          }
      });
  };

