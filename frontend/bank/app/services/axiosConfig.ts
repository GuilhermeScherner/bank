import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: "http://127.0.0.1:5000/"
});

axiosInstance.interceptors.request.use(async (config) => {
    return {
        ...config
    };
});

axiosInstance.interceptors.request.use((config) => {
    if (config.params) {
        const request = new URLSearchParams();
        for (const [key, value] of Object.entries<any>(config.params)) {
            if (Array.isArray(value)) {
                for (const item of value) request.append(key, item.toString());
            } else if (value !== undefined) {
                request.append(key, value);
            }
        }
        config.params = request;
    }
    return config;
});

axiosInstance.interceptors.request.use(async (config) => {
    let token = localStorage.getItem('token');

    if (!token) return config;

    config.headers.Authorization = `Bearer ${token}`;

    return config;
});


export default axiosInstance;
