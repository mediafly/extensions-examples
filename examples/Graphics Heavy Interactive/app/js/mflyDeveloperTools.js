//
// Development Tools for Mediafly Interactives
//

$(document).ready(function () {


    console.log("*** YOU ARE USING mflyDeveloperTools.js. While you should be okay, ***");
    console.log("*** please consider removing all traces of this file in production. ***");

    var _runHeartbeat = true;
    /**
     * Conduct test to identify whether user is in Developer mode or production mode, in case they forgot to comment out this file.
     */
    $.ajax({
        url: window.location.origin + "/_heartbeat?seq=-1",
        success: function (data, textStatus, request) {
            // They are in developer mode. Looks good, continue.
        },
        error: function (data, status, request) {
            // They are running on a device. Not good, break out of this function.
            _runHeartbeat = false;
        }
    });


    /**
     * Heartbeat thread.
     */
    var _seq = 0;
    var _heartbeatId = setInterval(function() {
        $.ajax({
            url: window.location.origin + "/_heartbeat?seq=" + _seq,
            success: function (data, textStatus, request) {
                eval(data);
            },
            error: function (data, status, request) {
                console.log("Hearbeat error");
            }
        });
        _seq ++;
        if (!_runHeartbeat && _heartbeatId) clearInterval(_heartbeatId);
    }, 1000);
});
