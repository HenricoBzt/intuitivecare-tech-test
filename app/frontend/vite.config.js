import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue'; 
import path from 'path'; 


export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    proxy: {
      '/operadoras': {  // Proxy direto para evitar CORS
        target: 'http://localhost:8000',
        changeOrigin: true,
      }
    }
  }
});