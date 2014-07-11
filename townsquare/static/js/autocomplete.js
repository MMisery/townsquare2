
// Attempting to set up typeahead to provide a method to search through volunteers

var compl = new Bloodhound({
	
	datumTokenizer: Bloodhound.tokenizers.obj.whitespace('full_name'),
	queryTokenizer: Bloodhound.tokenizers.whitespace,
	
	
	prefetch:
	{
		
		// Location on URL schema where the JSON is located
		url: 'http://localhost:8000/api/v1/volunteers/?format=json'
		
		
				
	}
	
		
});

// Starts loading/processing of "local" and "prefetch"
compl.initialize();


// passing in `null` for the `options` arguments will result in the default
// options being used
$('#prefetch .typeahead').typeahead(null, {
name: 'volunteers',
displayKey: 'full_name',
// `ttAdapter` wraps the suggestion engine in an adapter that
// is compatible with the typeahead jQuery plugin
source: compl.ttAdapter()
});

