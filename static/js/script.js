document.addEventListener('DOMContentLoaded', function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function() {
        console.log('Connected to server');
    });

    socket.on('notification', function(data) {
        var notifications = document.getElementById('notifications');
        var message = document.createElement('div');
        message.textContent = data.message;
        notifications.appendChild(message);
    });

    // Exemple d'envoi d'image (à adapter selon votre source d'image)
    var img = document.createElement('img');
    img.src = 'static/images/image2.jpg';
    img.onload = function() {
        var canvas = document.createElement('canvas');
        canvas.width = img.width;
        canvas.height = img.height;
        var ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0);
        var dataURL = canvas.toDataURL('image/jpeg');
        var binary = atob(dataURL.split(',')[1]);
        var array = [];
        for (var i = 0; i < binary.length; i++) {
            array.push(binary.charCodeAt(i));
        }
        var blob = new Blob([new Uint8Array(array)], {type: 'image/jpeg'});
        socket.emit('image', blob);
    };
});
