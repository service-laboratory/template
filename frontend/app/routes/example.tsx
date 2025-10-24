import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "{{ cookiecutter.project_name }}" },
    { name: "description", content: "Template for fast start new services" },
  ];
}

export default function Example() {
  return <h1>service template example</h1>;
}
