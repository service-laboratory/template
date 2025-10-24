import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Service template" },
    { name: "description", content: "Template for fast start new services" },
  ];
}

export default function Home() {
  return <h1>service template</h1>;
}
