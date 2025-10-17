import { LoginForm } from "@service_laboratory/auth";
import { useForm } from "react-hook-form";
import { Link } from "react-router";

export function meta() {
  return [{ title: "Login" }];
}

export default function LoginPage() {
  const form = useForm({
    defaultValues: {
      email: "",
      password: "",
    },
  });

  return (
    <div className="flex min-h-svh w-full items-center justify-center p-6 md:p-10">
      <div className="w-full max-w-sm">
        <LoginForm
          form={form}
          submit={(values) => {
            console.log(values);
          }}
          loginFormTitle="Login"
          loginFormDescription="Please enter your email and password to login."
          emailLabel="Email"
          passwordLabel="Password"
          forgotPasswordMessage="Forgot password?"
          submitButtonLabel="Login"
          resetPasswordLinkComponent={() => (
            <Link
              className="ml-auto inline-block text-sm underline-offset-4 hover:underline"
              to={"/reset-password"}
            >
              forgot password?
            </Link>
          )}
        />
      </div>
    </div>
  );
}
