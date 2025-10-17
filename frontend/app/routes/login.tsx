import { LoginForm } from "@service_laboratory/auth";

export function meta() {
  return [{ title: "Login" }];
}

export default function LoginPage() {
  return (
    <h1>
      <LoginForm />
    </h1>
  );
}
