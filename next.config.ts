import type { NextConfig } from "next";
const repo = "opsmirror-20260914";
const isPages = process.env.GITHUB_ACTIONS === "true" && process.env.NODE_ENV === "production";
const config: NextConfig = { output: "export", trailingSlash: true, images: { unoptimized: true }, ...(isPages ? { basePath: `/${repo}`, assetPrefix: `/${repo}/` } : {}) };
export default config;
