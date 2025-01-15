// Slideshow for Gallery and Testimonials

let currentImage = 0;
const images = document.querySelectorAll(".slideshow img");
let interval;

// Function to show the next image
function showNextImage() {
    images[currentImage].style.display = "none";
    currentImage = (currentImage + 1) % images.length;
    images[currentImage].style.display = "block";
}

// Start the slideshow with a 1-second delay
function startSlideshow() {
    interval = setInterval(showNextImage, 1000);  // Change image every 1 seconds
}

// Stop the slideshow
function stopSlideshow() {
    clearInterval(interval);
}

// Resume the slideshow
function resumeSlideshow() {
    startSlideshow();
}

// Initial call to start the slideshow
startSlideshow();

// Add event listeners to each image for mouse hover and touch events
images.forEach((image) => {
    image.addEventListener("mouseover", stopSlideshow);  // Stop on hover
    image.addEventListener("mouseout", resumeSlideshow); // Resume on mouse out
});

// Handle touch events for mobile devices
let isTouching = false;
document.querySelector(".slideshow").addEventListener("touchstart", function() {
    stopSlideshow();
    isTouching = true;
}, { passive: true });

document.querySelector(".slideshow").addEventListener("touchend", function() {
    if (isTouching) {
        resumeSlideshow();
        isTouching = false;
    }
}, { passive: true });
