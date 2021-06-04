//Making the modal work
let imgPosts = document.querySelectorAll('.img-wrapper>img');
let postModal = document.querySelector('.modal');
let closeModalBtn = document.querySelector('.close-modal-btn');

imgPosts.forEach(function (imgPost) {
	imgPost.addEventListener('click', showPost);
});

postModal.addEventListener('click', function (event) {
	if (event.target == postModal) {
		hidePost();
	}
});

closeModalBtn.addEventListener('click', hidePost);
document.addEventListener('keydown', function (e) {
	if (e.key === 'Escape') hidePost();
});

function showPost() {
	postModal.style.display = 'flex';
	document.body.style.overflowY = 'hidden';
}

function hidePost(event) {
	postModal.style.display = 'none';
	document.body.style.overflowY = 'auto';
}

// Switching active nav tabs
let navTabs = document.querySelectorAll('.nav-tab');
let activeNavTab = document.querySelector('.active-nav-tab');

navTabs.forEach(function (tab) {
	tab.addEventListener('click', switchTab);
});

function switchTab(event) {
	let tab = event.target;

	activeNavTab.classList.remove('active-nav-tab');
	tab.classList.add('active-nav-tab');

	activeNavTab = tab;
}
