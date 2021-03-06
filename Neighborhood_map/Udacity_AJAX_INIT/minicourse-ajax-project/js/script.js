
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');
    
    var streetStr = $('#street').val();
    var cityStr = $('#city').val();
    var address = streetStr + ', ' + cityStr;

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview

    // YOUR CODE GOES HERE!
      var streetViewUrl = 'http://maps.googleapis.com/maps/api/streetview?size=600x300&location=' + 
        address + '';
    
    $greeting.text=('So you want to live at ' +  address + '?');
    
    var finalURL = '<img class="bgimg" src="' + streetViewUrl + '">';
    
    $body.append(finalURL);
    
    
    var nyturl = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    nyturl += '?' + $.param({
        'api-key': "4e90beed50a7481babc203e18bfd3b25"
        })


    $nytHeaderElem.text('NYT articles about ' + cityStr);
    var data
    $.getJSON( nyturl, data, function( data ) {
        
        console.log(data);
        var items = [];
        docs = data["response"]["docs"];
        $.each( docs, function( key, val ) {
            
            var t1 = val["headline"];
            var t2 = t1["main"];
            
            var nurl = val["web_url"];
            
            items.push( "<li id='" + key + "'>" + "<a href=" + nurl + ">" + t2 +"</a>"+"</li>" );
            
        });

        $( "<ul/>", {
        "class": "my-new-list",
        html: items.join( "" )
        
        }).appendTo( "#nytimes-header" );
        
        
        
    }).error(function() {
            $nytHeaderElem.text('NYT articles could NOT be loaded');
          });; 

    
    var wikiUrl = 'http://en.wikipedia.org/w/api.php?action=opensearch&';
    wikiUrl += 'search=' + cityStr + '&format=json&callback=wikiCallback';

    var wikiReqTimeout = setTimeout(function(){
        $wikiElem.text("failed to get wikipedia resources");
    },8000);

    $.ajax({
        url: wikiUrl,
          dataType: "jsonp",
          success: function (response) {
              // body...
              var articleList = response[1];
              console.log(articleList);
              console.log(articleList.length);
              var i=0;
              for (;i <  articleList.length; i++) {
                articleStr = articleList[i];
                var aurl = 'http://en.wikipedia.org/wiki/' + articleStr;
                $wikiElem.append(
                    '<li><a href="' + aurl + '">' + articleStr+ '</a></li>'
                    );
              }

              clearTimeout(wikiReqTimeout);
          }

    }); 

    return false;
};

$('#form-container').submit(loadData);
