function validate(FORM) {
	var fields = {};

	fields['Team Name'] = FORM.tn;
	fields['Short Description'] = FORM.shortdesc;

	for( label in fields ) {
		input = fields[label];
		// null strings and spaces only strings not allowed
		if(/(^$)|(^\s+$)/.test(input.value)) {
			input.focus();
			alert("Please enter a "+label+".");
			return false;
		}
	}

	return true;
}

