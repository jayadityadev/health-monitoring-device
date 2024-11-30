import { defineConfig } from 'vite';

export default defineConfig({
    server: {
        proxy: {
            '/patients_data': {
                target: 'http://localhost:8000',
                changeOrigin: true,
                rewrite: (path) => path.replace(/^\/patients_data/, '/patients_data'),
            },
        },
    },
});
