from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for countries, universities, testimonials, and gallery
countries = [
    {"name": "USA", "flag": "https://cdn.britannica.com/82/682-004-F0B47FCB/Flag-France.jpg"},
    {"name": "UK", "flag": "https://media.hswstatic.com/eyJidWNrZXQiOiJjb250ZW50Lmhzd3N0YXRpYy5jb20iLCJrZXkiOiJnaWZcL2dldHR5aW1hZ2VzLTIxNjMyMDA3MDItMS5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjgyOH19fQ=="},
    {"name": "Canada", "flag": "https://flagsireland.com/cdn/shop/products/CanadaFlag.png?v=1678435840"},
    {"name": "India", "flag": "https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/1200px-Flag_of_India.svg.png"},
    {"name": "Australia", "flag": "https://media.istockphoto.com/id/1092635968/vector/australia-flag.jpg?s=612x612&w=0&k=20&c=YEp_hCl7Ub0nteWFKh6HrZwSFzUh3xmEYWuJe-RRt5Y="}
]
country_icons = [
    {"name": "France", "image": "https://cdn.britannica.com/82/682-004-F0B47FCB/Flag-France.jpg"},
    {"name": "Japan", "image": ""},
    {"name": "USA", "image": "https://cdn.britannica.com/79/4479-050-6EF87027/flag-Stars-and-Stripes-May-1-1795.jpg"},
    {"name": "Australia", "image": "https://media.istockphoto.com/id/1092635968/vector/australia-flag.jpg?s=612x612&w=0&k=20&c=YEp_hCl7Ub0nteWFKh6HrZwSFzUh3xmEYWuJe-RRt5Y="}
]

universities = [
    {"name": "Harvard University", "image": "https://www.avanse.com/blogs/images/What%20you%20must%20know%20about%20Harvard%20University.jpg", "tuition": "$50,000 per year"},
    {"name": "Oxford University", "image": "https://c.files.bbci.co.uk/2c03/live/64d39070-8596-11ef-addc-5556603eb4c1.jpg", "tuition": "$45,000 per year"},
    {"name": "MIT", "image": "https://news.mit.edu/sites/default/files/styles/news_article__image_gallery/public/images/202407/MIT-MIssion-Leads-01-press_0.jpg?itok=Rn8dR3W5", "tuition": "$53,000 per year"}
]


destination_images = [
    "https://scontent.fdac14-1.fna.fbcdn.net/v/t39.30808-6/469263870_122123463476564633_9174799633307171266_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=111&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeFmVm7wfiZuzr3oMxPNJfm4ICl4G9f4BTYgKXgb1_gFNsTY_KTvlkjm014NC90MqL9NHI-9ToSSHJQQxmF0orBa&_nc_ohc=7jwyMm2YGOYQ7kNvgE5Kcrj&_nc_zt=23&_nc_ht=scontent.fdac14-1.fna&_nc_gid=ANef4KUH3cbkTFfNT3xwYqC&oh=00_AYB5yYMQI9gws71DbKGHECiHK-D25GpNaxqUsptyTcWI1g&oe=678C57DA",
    "https://scontent.fdac14-1.fna.fbcdn.net/v/t39.30808-6/470665050_122126238884564633_5385689614305390637_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=102&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeHErwQC2gFtg4uLF3h19B1CsNPLZdpZez-w08tl2ll7P5gYTtqpZhwyzNbU9W687DLmzCEGEHk5afZ8mBnDldx5&_nc_ohc=ZRzJ-T0qSMoQ7kNvgEbfcTA&_nc_zt=23&_nc_ht=scontent.fdac14-1.fna&_nc_gid=AApg2pQtawsWFN1bxptAfvF&oh=00_AYDEwC6ZD2KviqaBE4GZ9t7rSgSAfT9RKY3NvIhPCtbn0Q&oe=678C7A24",
    "https://scontent.fdac14-1.fna.fbcdn.net/v/t39.30808-6/469198852_122123446382564633_3448725639995244727_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=101&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeFc0yR7OH_IPXdtbMHNqqSFGIwyjyBFnMoYjDKPIEWcyjocvByWQ4kirSh3ZT7Hcs53lDnPaW6qyrLaZ97y-VdF&_nc_ohc=0QCulDoRvUoQ7kNvgHTzK3H&_nc_zt=23&_nc_ht=scontent.fdac14-1.fna&_nc_gid=AB6pBfuqYyMdhMnGO7ET8Gq&oh=00_AYD2if9DE86wBzgHjunL-F7SK3sG9B1dndh-5Jc6-uug-g&oe=678C693D"
]
gallery_images = [
    "https://scontent.fdac14-1.fna.fbcdn.net/v/t39.30808-6/469263870_122123463476564633_9174799633307171266_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=111&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeFmVm7wfiZuzr3oMxPNJfm4ICl4G9f4BTYgKXgb1_gFNsTY_KTvlkjm014NC90MqL9NHI-9ToSSHJQQxmF0orBa&_nc_ohc=7jwyMm2YGOYQ7kNvgE5Kcrj&_nc_zt=23&_nc_ht=scontent.fdac14-1.fna&_nc_gid=ANef4KUH3cbkTFfNT3xwYqC&oh=00_AYB5yYMQI9gws71DbKGHECiHK-D25GpNaxqUsptyTcWI1g&oe=678C57DA",
    "https://scontent.fdac14-1.fna.fbcdn.net/v/t39.30808-6/469263870_122123463476564633_9174799633307171266_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=111&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeFmVm7wfiZuzr3oMxPNJfm4ICl4G9f4BTYgKXgb1_gFNsTY_KTvlkjm014NC90MqL9NHI-9ToSSHJQQxmF0orBa&_nc_ohc=7jwyMm2YGOYQ7kNvgE5Kcrj&_nc_zt=23&_nc_ht=scontent.fdac14-1.fna&_nc_gid=ANef4KUH3cbkTFfNT3xwYqC&oh=00_AYB5yYMQI9gws71DbKGHECiHK-D25GpNaxqUsptyTcWI1g&oe=678C57DA",
    "https://scontent.fdac14-1.fna.fbcdn.net/v/t39.30808-6/469198852_122123446382564633_3448725639995244727_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=101&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeFc0yR7OH_IPXdtbMHNqqSFGIwyjyBFnMoYjDKPIEWcyjocvByWQ4kirSh3ZT7Hcs53lDnPaW6qyrLaZ97y-VdF&_nc_ohc=0QCulDoRvUoQ7kNvgHTzK3H&_nc_zt=23&_nc_ht=scontent.fdac14-1.fna&_nc_gid=AB6pBfuqYyMdhMnGO7ET8Gq&oh=00_AYD2if9DE86wBzgHjunL-F7SK3sG9B1dndh-5Jc6-uug-g&oe=678C693D"
]
testimonials = [
    {"name": "Nasi", "feedback": "Amazing experience! Highly recommend this travel agency.", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqkUYrITWyI8OhPNDHoCDUjGjhg8w10_HRqg&s"},
    {"name": "Nusrat", "feedback": "Had a great time! They really took care of everything.", "image": "https://png.pngtree.com/png-vector/20221209/ourmid/pngtree-bangladesh-flag-silver-and-gold-circle-button-design-free-vector-png-image_6516928.png"},
    {"name": "Ibra", "feedback": "Top-notch service, would book again.", "image": "https://media.istockphoto.com/id/1411901680/photo/happy-man-toothy-smile-positive-emotion-avatar.jpg?s=612x612&w=0&k=20&c=H7YtE74Fs0CuGYftk0UtPYdZtO3VgBF5cX2HYmCI0C4="}
]

videos = [
    {"title": "Explore USA", "url": "https://videos.pexels.com/video-files/7235653/7235653-hd_1920_1080_30fps.mp4"},
    {"title": "Tour Europe", "url": "https://videos.pexels.com/video-files/8060929/8060929-hd_1920_1080_25fps.mp4"}
]

@app.route('/')
def index():
    return render_template('index.html', countries=countries, universities=universities, gallery_images=gallery_images, testimonials=testimonials, videos=videos)

@app.route('/book-now', methods=['POST'])
def book_now():
    name = request.form['name']
    email = request.form['email']
    destination = request.form['destination']
    print(f"Booking Request - Name: {name}, Email: {email}, Destination: {destination}")
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
