"use client";

import styles from "./page.module.css";
import { useRouter } from 'next/navigation';
import MyButton from './components/button';

export default function App() {
  const router = useRouter();

  function clickTraining() {
    console.log("Training started");
    router.push("/pages/cards");
  }

  function clickReview() {
    console.log("Review started");
    router.push("/pages/review");
  }

  return (
    <>
      <div className={styles.page}>
        <main className={styles.main}>

          <h1 className={styles.title}>
            Welcome to the Vocable Trainer App!
          </h1>
          <div className={styles.buttonContainer}>
            <MyButton title="Lerne neue Vokables" onClickButton={clickTraining} />
            <MyButton title="Review deine Vokables" onClickButton={clickReview} />
            <MyButton title="Deine Vokables-Statistik (Coming Soon)" onClickButton={() => console.log('Statistics clicked')} />
          </div>
        </main>
        <footer className={styles.footer}>
        </footer>
      </div>
    </>
  );
}
