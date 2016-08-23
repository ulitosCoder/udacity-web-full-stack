
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');
    
    var streetStr = $('#street').val();
    var cityStr = $('#city').val();
    var address = streetStr + ', ' + cityStr;
    
  ;

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
    
    return false;
};

$('#form-container').submit(loadData);
