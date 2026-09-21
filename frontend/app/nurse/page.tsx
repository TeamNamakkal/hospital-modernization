import Link from "next/link";

export default function NursePage() {
  return (
    <div className="flex min-h-screen flex-col items-center bg-zinc-50 px-6 py-16 font-sans dark:bg-black">
      <main className="w-full max-w-2xl">
        <Link href="/" className="text-sm text-zinc-500 hover:underline">
          &larr; Back
        </Link>
        <h1 className="mt-4 text-2xl font-semibold text-black dark:text-zinc-50">
          Nurse Intake
        </h1>
        <p className="mt-2 text-zinc-600 dark:text-zinc-400">
          Coming soon: vitals entry, insurance details, and report upload.
        </p>
      </main>
    </div>
  );
}
