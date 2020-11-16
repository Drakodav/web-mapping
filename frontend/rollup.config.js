import workbox from 'rollup-plugin-workbox-build';
import typescript from 'rollup-plugin-typescript';
import { uglify } from "rollup-plugin-uglify";


export default {
  input: './index.ts',
  output: {
    file: './dist/bundle.js',
    format: 'iife',
    name: 'bundle'
  },
  plugins: [
    typescript(),
    uglify(),
    workbox({
      mode: 'generateSW', // or 'injectManifest'
      options: {
        swDest: './dist/service-worker.js',
        globDirectory: './dist',
        // other workbox-build options depending on the mode
      },
    }),
  ],
  external: ['workbox-routing', 'workbox-strategies', 'workbox-expiration']
};
