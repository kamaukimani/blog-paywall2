
import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/articles': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
      '/login': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
      '/logout': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
      '/check_session': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
      '/clear': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
      '/members_only_articles': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
    },
  },
});
