.class public Lcom/njctf/mobile/easycrack/MainActivity;
.super Landroid/support/v7/app/AppCompatActivity;
.source "MainActivity.java"


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/njctf/mobile/easycrack/MainActivity$CheckText;
    }
.end annotation


# direct methods
.method static constructor <clinit>()V
    .locals 1

    .prologue
    .line 14
    const-string v0, "native-lib"

    invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V

    .line 15
    return-void
.end method

.method public constructor <init>()V
    .locals 0

    .prologue
    .line 10
    invoke-direct {p0}, Landroid/support/v7/app/AppCompatActivity;-><init>()V

    return-void
.end method


# virtual methods
.method public messageMe()Ljava/lang/String;
    .locals 10

    .prologue
    .line 45
    const-string v3, ""

    .line 46
    .local v3, "result":Ljava/lang/String;
    const/16 v4, 0x33

    .line 47
    .local v4, "t":I
    invoke-virtual {p0}, Lcom/njctf/mobile/easycrack/MainActivity;->getApplicationContext()Landroid/content/Context;

    move-result-object v5

    invoke-virtual {v5}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v5

    const-string v6, "\\."

    invoke-virtual {v5, v6}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v1

    .line 48
    .local v1, "paname":[Ljava/lang/String;
    array-length v5, v1

    add-int/lit8 v5, v5, -0x1

    aget-object v2, v1, v5

    .line 50
    .local v2, "pname":Ljava/lang/String;
    invoke-virtual {v2}, Ljava/lang/String;->toCharArray()[C

    move-result-object v6

    array-length v7, v6

    const/4 v5, 0x0

    :goto_0
    if-ge v5, v7, :cond_0

    aget-char v0, v6, v5

    .line 51
    .local v0, "ch":C
    xor-int/2addr v4, v0

    .line 52
    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v8, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v8

    int-to-char v9, v4

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    move-result-object v8

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    .line 50
    add-int/lit8 v5, v5, 0x1

    goto :goto_0

    .line 54
    .end local v0    # "ch":C
    :cond_0
    return-object v3
.end method

.method protected onCreate(Landroid/os/Bundle;)V
    .locals 3
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .prologue
    .line 19
    invoke-super {p0, p1}, Landroid/support/v7/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    .line 20
    const v2, 0x7f04001b

    invoke-virtual {p0, v2}, Lcom/njctf/mobile/easycrack/MainActivity;->setContentView(I)V

    .line 23
    const v2, 0x7f0b0058

    invoke-virtual {p0, v2}, Lcom/njctf/mobile/easycrack/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/TextView;

    .line 24
    .local v1, "tv":Landroid/widget/TextView;
    invoke-virtual {p0}, Lcom/njctf/mobile/easycrack/MainActivity;->stringFromJNI()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 26
    const v2, 0x7f0b0057

    invoke-virtual {p0, v2}, Lcom/njctf/mobile/easycrack/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/EditText;

    .line 27
    .local v0, "textparse":Landroid/widget/EditText;
    new-instance v2, Lcom/njctf/mobile/easycrack/MainActivity$CheckText;

    invoke-direct {v2, p0}, Lcom/njctf/mobile/easycrack/MainActivity$CheckText;-><init>(Lcom/njctf/mobile/easycrack/MainActivity;)V

    invoke-virtual {v0, v2}, Landroid/widget/EditText;->addTextChangedListener(Landroid/text/TextWatcher;)V

    .line 28
    return-void
.end method

.method public native parseText(Ljava/lang/String;)Ljava/lang/String;
.end method

.method public native stringFromJNI()Ljava/lang/String;
.end method
