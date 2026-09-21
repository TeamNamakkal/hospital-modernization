import Link from "next/link";

const ROLES = [
  {
    href: "/signup",
    title: "Front Desk / Patient",
    description: "Create patient, start visit, view queue status",
  },
  {
    href: "/queue",
    title: "Queue",
    description: "Live queue status for all clinical roles",
  },
  {
    href: "/nurse",
    title: "Nurse",
    description: "Open queued patient, enter vitals, upload report",
  },
  {
    href: "/doctor",
    title: "Doctor",
    description: "Review record, dictate/edit/approve note, create order",
  },
];

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center bg-zinc-50 px-6 py-16 font-sans dark:bg-black">
      <main className="w-full max-w-2xl">
        <h1 className="text-3xl font-semibold tracking-tight text-black dark:text-zinc-50">
          Hospital Modernization — MVP
        </h1>
        <p className="mt-2 text-zinc-600 dark:text-zinc-400">
          Patient Signup → Queue → Nurse Intake → Doctor Consultation → Voice
          Note → AI Rewrite → Doctor Approval → Lab/Prescription Order
        </p>

        <div className="mt-10 grid gap-4 sm:grid-cols-2">
          {ROLES.map((role) => (
            <Link
              key={role.href}
              href={role.href}
              className="rounded-lg border border-black/[.08] p-5 transition-colors hover:bg-black/[.04] dark:border-white/[.145] dark:hover:bg-white/[.06]"
            >
              <h2 className="font-medium text-black dark:text-zinc-50">
                {role.title}
              </h2>
              <p className="mt-1 text-sm text-zinc-600 dark:text-zinc-400">
                {role.description}
              </p>
            </Link>
          ))}
        </div>
      </main>
    </div>
  );
}
