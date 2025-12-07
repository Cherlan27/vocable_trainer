"use client";

import styles from "./page.module.css";
import { useRouter } from 'next/navigation';
import { MyButton } from './components/button';

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
            <MyButton title="Learn new Vocables" onClickButton={clickTraining} />
            <MyButton title="Review learnd Vocables" onClickButton={clickReview} />
            <MyButton title="Your Vocables statistics (Coming Soon)" onClickButton={() => console.log('Statistics clicked')} />
          </div>
        </main>
        <footer className={styles.footer}>
        </footer>
      </div>
    </>
  );
}
