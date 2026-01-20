"use client";

import { useRouter } from 'next/navigation';
import { useState } from "react";
import { MyButton, MyButton2 } from "@/app/components/button";
import InputField from "@/app/components/input";
import styles from "../page.module.css";
import "./page_style.css";

export default function ManualVoc() {
    const router = useRouter();
    const [englishVoc, setEnglishVoc] = useState<string>("");
    const [frenchVoc, setFrenchVoc] = useState<string>("");

    function sendVocables(
        english: string,
        french: string
    ) {
        console.log("New vocable send");
    }

    return (
        <div className={styles.page}>
      <main className={styles.main}>
        <div className="container">
          <h1>Cards Page</h1>
          <p>Learn new vocables!</p>
          <div style={{
            height: '40px',
            width: '100%',
            marginBottom: '30px',
            marginTop: '10px',
            display: 'flex',
            flexDirection: 'row',
            gap: '10px',
            alignItems: 'center',
            justifyContent: 'center',
          }}>
            <input
                type="text"
                placeholder="English"
                className="input input-bordered w-full max-w-xs"
                value={englishVoc}
                onChange={(e) => setEnglishVoc(e.target.value)}
            />
            <input
                type="text"
                placeholder="French"
                className="input input-bordered w-full max-w-xs"
                value={frenchVoc}
                onChange={(e) => setFrenchVoc(e.target.value)}
            />
            <MyButton2 title="Process" onClickButton={() => sendVocables(englishVoc, frenchVoc)} id="Input-Button"/>
          </div>
          <MyButton title="Back to Home" onClickButton={() => router.push('/')} />
        </div>
      </main>
    </div>
    )
}
