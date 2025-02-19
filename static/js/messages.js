let $ = document;
const notifications = $.querySelector(".notifications");

const toastDetails = {
	timer: 5000,
	success: { icon: "fa-circle-check" },
	error: { icon: "fa-circle-xmark" },
	warning: { icon: "fa-circle-exclamation" },
	info: { icon: "fa-circle-info" }
};

const removeToast = (toast) => {
	toast.classList.add("hide");
	if (toast.timeoutId) clearTimeout(toast.timeoutId);
	setTimeout(() => toast.remove(), 500);
};

const createToast = (type, text) => {
	if (!toastDetails[type]) return;
	const { icon } = toastDetails[type];
	const toast = $.createElement("li");
	toast.className = `toast ${type}`;
	toast.innerHTML = `<div class="column">
							<i class="fa-solid ${icon}"></i>
							<span>${text}</span>
						</div>
						<i class="fa-solid fa-xmark" onclick="removeToast(this.parentElement)"></i>`;
	notifications.appendChild(toast);
	toast.timeoutId = setTimeout(() => removeToast(toast), toastDetails.timer);
};


