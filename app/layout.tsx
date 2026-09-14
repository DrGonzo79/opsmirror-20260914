import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "OpsMirror — SOP reality check", description: "Compare written refund policy with what support teams actually did." };
export default function RootLayout({children}:{children:React.ReactNode}) { return <html lang="en"><body>{children}</body></html>; }
