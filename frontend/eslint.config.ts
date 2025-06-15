import pluginVue from 'eslint-plugin-vue'
import typescript from '@typescript-eslint/eslint-plugin'
import parser from '@typescript-eslint/parser'
import skipFormatting from '@vue/eslint-config-prettier/skip-formatting'

export default [
  {
    files: ['**/*.{ts,mts,tsx,vue}'],
    ignores: ['**/dist/**', '**/dist-ssr/**', '**/coverage/**'],
    plugins: {
      vue: pluginVue,
      '@typescript-eslint': typescript
    },
    languageOptions: {
      parser: require('vue-eslint-parser'),
      parserOptions: {
        parser,
        ecmaVersion: 'latest'
      }
    },
    rules: {
      ...pluginVue.configs['flat/essential'][0].rules,
      ...typescript.configs['recommended'].rules
    }
  },
  skipFormatting
]