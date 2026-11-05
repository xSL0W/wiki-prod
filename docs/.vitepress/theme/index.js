// .vitepress/theme/index.js
import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import NotFound from './Custom/NotFound.vue'
import '@fontsource-variable/inter'
import './style.css'

/** @type {import('vitepress').Theme} */
export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      'not-found': () => h(NotFound),
    })
  },
  enhanceApp({ app, router, siteData }) {
        if (typeof window !== 'undefined' && 'navigation' in window) {
      window.navigation.addEventListener('navigate', (event) => {
        // Prevent bfcache issues by forcing reload on back/forward navigation
        if (event.navigationType === 'back_forward') {
          window.location.reload();
        }
      });
    }
  }
}
