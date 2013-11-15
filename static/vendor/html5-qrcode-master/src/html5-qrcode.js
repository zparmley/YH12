(function( $ ){

  $.fn.html5_qrcode = function(qrcodeSuccess, qrcodeError, videoError) {
    'use strict';

    var height = this.height() || 250;
    var width = this.width() || 300;

	// only add the vid in if it's not there already
	if ($(this).children().length == 0) {
		var vidTag = '<video id="html5_qrcode_video" width="' + width + 'px" height="' + height + 'px"></video>' 
		var canvasTag = '<canvas id="qr-canvas" width="' + (width - 2) + 'px" height="' + (height - 2) + 'px" style="display:none;"></canvas>' 

		this.append(vidTag);
		this.append(canvasTag);
	}


    var video = $('#html5_qrcode_video').get(0);
    var canvas;
    var context;

    $('#qr-canvas').each(function(index, element) {
        canvas = element;
        context = element.getContext('2d');
    });


    var scan = function() {
      if (window.localMediaStream) {
        context.drawImage(video, 0, 0, 307,250);

        try {
          qrcode.decode();
        } catch(e) {
          qrcodeError(e);
        }

        setTimeout(scan, 500);

      } else {
        setTimeout(scan, 500);
      }
    }


    window.URL = window.URL || window.webkitURL || window.mozURL || window.msURL;
    navigator.getUserMedia  = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;

    var successCallback = function(stream) {
        video.src = (window.URL && window.URL.createObjectURL(stream)) || stream;
        window.localMediaStream = stream;

        video.play();
        setTimeout(scan,1000);
    }

    if (navigator.getUserMedia) {
        navigator.getUserMedia({video: true}, successCallback, videoError);
    } else {
        console.log('Native web camera streaming (getUserMedia) not supported in this browser.');
    }

    qrcode.callback = qrcodeSuccess;

  };
})( jQuery );
