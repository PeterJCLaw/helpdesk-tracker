function updateStatus(code) {
	if (code == 1) {
		$("#op").attr("checked", "true");
	} else if (code == 2) {
		$("#og").attr("checked", "true");
	} else if (code == 4) {
		$("#c").attr("checked", "true");
	}
}

function updateAssigned(assignedTo) {
	$("#assigninput").attr("value", assignedTo);
}

function pull() {
	$.get(BASE_URL+'issuejson/'+ID+'/', function(data) {
		var issue = eval('(' + data + ')');
		//alert(issue.description);
		$("#desc").html(issue.description.replace("\\\\n", "cow"));
		$("#touched").html("Last Touched: " + issue.touched)
		log('Updating');
		log("lastClick: "+(time()-lastClick)+' ago');

		if (lastUpdated + 300 > new Date().getTime() || overwriteInput == 1) {
			log("cows2");
			updateStatus(issue.status);
			updateAssigned(issue.assigned);
			overwriteInput = 1;
		} else {
			log('too much recent activity -- bailing');
		}

	});
}

function time() {
	return Math.round(new Date().getTime() / 1000);
}

function noinputOverwrite (data) {
       log("*click*");
	lastUpdated = new Date().getTime();
}

var overwriteInput = 1;
var lastUpdated = new Date().getTime();

function init() {
	$("input").bind("focusin", noinputOverwrite);
	$("textarea").bind("focusin", noinputOverwrite);
	$("input").bind("select", noinputOverwrite);
	setInterval(pull,1500);
}

var dont_log = true;
function log(what) {
	if( dont_log && typeof console != 'object')
		return;
	dont_log = false;
	console.log(what);
}
function dir(what) {
	if( dont_log && typeof console != 'object')
		return;
	dont_log = false;
	console.dir(what);
}

