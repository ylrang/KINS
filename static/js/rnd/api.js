window.onload = async function loadPage() {
    const response = await fetch('/api/regulations', {
        headers: {
            'content-type': 'application/json',
        },
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        console.log('data', data);
        let regulations = '';
        data.forEach(reg => {
            regulations += `<div class="card mt-2">
                        <div class="card-body p-4">
                            <div class="" style="display:flex; justify-content:space-between">
                                <div>
                                    <h5 class="post-title fs-17 mb-0">
                                        <a href="/regulation_detail${reg.pk}" class="primary-link">${reg.title} </a>
                                    </h5>
                                </div>
                                <ul class="list-inline mb-0 text-muted">
                                    <li class="list-inline-item">
                                        <i class="mdi mdi-calendar-clock"></i> ${reg.creation_date} 
                                        <i class="mdi mdi-account-circle"></i> ${reg.writer} 
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>`;
            });
            document.getElementById('regulations').innerHTML = regulations;
        })
}