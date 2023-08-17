
document.addEventListener('DOMContentLoaded', function() {
    const videoIframe = document.querySelector('.iframe-container iframe');
    const videoHeight = videoIframe.offsetHeight;
    
    const videoList = document.getElementById('vedio_list');
    videoList.style.maxHeight = `${videoHeight}px`;
});

