import { defineConfig } from "vite";
import dts from "vite-plugin-dts";
import viteReact from "@vitejs/plugin-react";
import path from "path";

export default defineConfig({
  plugins: [dts({ rollupTypes: true }), viteReact()],
  build: {
    lib: {
      entry: "./src/index.ts",
      name: "index",
      fileName: "index",
    },
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
});
