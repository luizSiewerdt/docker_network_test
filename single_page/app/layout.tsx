export const metadata = {
  title: "Single Page",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-br">
      <body style={{ fontFamily: "sans-serif", margin: "2rem" }}>{children}</body>
    </html>
  );
}
