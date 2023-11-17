//<video id="videoPlayer" controls>
 //   <!-- Aquí mostrarás el video -->
//</video>

//<!-- Enlaces de lección -->
//<a class="lesson-link" data-video-url="{{ leccion.video_url }}" href="#">Lección 1</a>
//<a class="lesson-link" data-video-url="{{ otra_leccion.video_url }}" href="#">Lección 2</a>

    // Capturar el evento de clic en los enlaces de lección
 
 
 
 
    const lessonLinks = document.querySelectorAll(".lesson-link");
    const videoPlayer = document.getElementById("video");

    lessonLinks.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            const videoUrl = this.getAttribute("data-video-url");

            // Actualizar el reproductor de video con la URL de la lección seleccionada
            videoPlayer.src = videoUrl;
        });
    });
