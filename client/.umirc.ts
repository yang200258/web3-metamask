import { defineConfig } from 'umi';

export default defineConfig({
  nodeModulesTransform: {
    type: 'none',
  },
  routes: [
    { path: '/', component: '@/pages/index' },
  ],
  fastRefresh: {},
  proxy: {
    '/rest': {
      target: 'http://127.0.0.1:9988/',
      changeOrigin: true,
      secure: false,
    },  
  }
});
