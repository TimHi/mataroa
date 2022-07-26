// keep timeout ids in an array so we reset them
var TIMEOUT_IDS = [];

// save post title and body as a Snapshot connected to current user
function saveLogEntry() {
    console.log("saving...");
    var title = document.getElementById('id_title').value;
    var body = document.getElementById('id_body').value;

    // prepare form data
    var formData = new FormData();
    formData.append("title", title);
    formData.append("body", body);

    // upload request
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function alertContents() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                console.log("success");
                // success, show feedback
            } else {
                console.log("failure");
                // failure, show feedback
            }
        } else {
            // this branch runs first
            // uplading, show feedback
            console.log("uplading...");
        }
    };

    xhr.open('POST', '/snapshots/create/');
    xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');
    xhr.send(formData);
}

// clear timeout ids from given array
function clearTimeoutList(timeoutList) {
    timeoutList.forEach(function (timeoutId) {
        clearTimeout(timeoutId);
    });
}

// listen for body textarea changes
function initAutoSave() {
    document.getElementById('id_body').addEventListener('keyup', function () {
        clearTimeoutList(TIMEOUT_IDS);
        var timeoutId = setTimeout(saveLogEntry, 2500);
        TIMEOUT_IDS.push(timeoutId);
    });
}

// init
// enable only for superusers for now
{% if request.user.is_superuser %}
initAutoSave();
{% endif %}
